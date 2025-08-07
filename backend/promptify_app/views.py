from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from promptify_app.models import Chat, ChatMessage
from promptify_app.serializers import ChatMessageSerializer, ChatSerializer
from django.utils import timezone
from datetime import timedelta
from google import genai


# Create your views here.
# client = OpenAI()
client = genai.Client()


now = timezone.now()
today = now.date()
yesterday = today - timedelta(days=1)
seven_days_ago = today - timedelta(days=7)
thirty_days_ago = today - timedelta(days=30)


# def createChatTitle(user_message):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "assistant", "content": "Give a short, descriptive title for this conversation in not more than 5 words."},
#                 {"role": "user", "content": user_message},
#             ]
#         )
#         title = response.choices[0].message.content.strip()
#     except Exception: 
#         title = user_message[:50]
#     return title


def createChatTitle(user_message):
    try:
        response = client.generate_content(
            model="gemini-2.5-flash",
            contents=f"Give a short, descriptive title for this conversation: '{user_message}'. Keep it under 4 words."
        )
        title = response.text.strip()
    except Exception:
        title = user_message[:50]
    return title


@api_view(['POST'])
def prompt_gemini(request):
    chat_id = request.data.get("chat_id")
    content = request.data.get("content")

    if not chat_id:
        return Response({"error": "Chat ID was not provided."}, status=400)

    if not content:
        return Response({"error": "There was no prompt passed."}, status=400)

    chat, created = Chat.objects.get_or_create(id=chat_id)
    chat.title = createChatTitle(content)
    chat.save()

    ChatMessage.objects.create(role="user", chat=chat, content=content)

    chat_messages = chat.messages.order_by("created_at")[:10]

    gemini_history = []
    for message in chat_messages:
        gemini_history.append({
            "role": message.role,
            "parts": [{"text": message.content}]
        })

    # Add assistant priming if not present
    if not any(message["role"] == "model" for message in gemini_history):
        gemini_history.insert(0, {
            "role": "model",
            "parts": [{"text": "You are a helpful assistant."}]
        })

    try:
        chat_session = client.chats.create(
            model="gemini-2.5-flash",
            history=gemini_history
        )

        gemini_response = chat_session.send_message(content)
        gemini_reply = gemini_response.text

    except Exception as e:
        return Response({"error": f"An error from Gemini: {str(e)}"}, status=500)

    ChatMessage.objects.create(role="model", content=gemini_reply, chat=chat)
    return Response({"reply": gemini_reply}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_chat_messages(request, pk):
    # chat = Chat.objects.get(id=pk)
    chat = get_object_or_404(Chat, id=pk)
    chatmessages = chat.messages.all()
    serializer = ChatMessageSerializer(chatmessages, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def todays_chat(request):
    chats = Chat.objects.filter(created_at__date=today).order_by("-created_at")[:10]
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def yesterdays_chat(request):
    chats = Chat.objects.filter(created_at__date=yesterday).order_by("-created_at")[:10]
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def seven_days_chat(request):
    chats = Chat.objects.filter(created_at__lt=yesterday, created_at__gte=seven_days_ago).order_by("-created_at")[:10]
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)