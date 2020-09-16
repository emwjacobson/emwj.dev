from django.shortcuts import render
from django.http import HttpResponse

projects = [
    {
        'image': 'https://i.imgur.com/THug83T.png',
        'title': 'MCHost',
        'description': 'This project aims to create on-demand Minecraft Servers. I used Docker in order to streamline development and make the creation/destruction of servers extremely easy. I used Django as the Frontend as I wanted to learn more about it.',
        'technologies': [
            "Docker & Docker-Compose",
            "Django"
        ],
        'links': [
            { 'text': 'Demo', 'url': 'https://mc.emwj.dev/' },
            { 'text': 'GitHub', 'url': 'https://github.com/emwjacobson/MCHoster'}
        ]
    },
]

def index(request):
    return render(request, 'app/index.html', {'projects': projects})
