from django.shortcuts import render
from django.http import HttpResponse

projects = [
    {
        'image': 'https://i.imgur.com/lv9cuij.png',
        'title': 'This Website!',
        'description': 'With a bit of downtime between my Summer Research Program and my first Quarter at UC Riverside, I decided it was time to make myself a basic little portfolio website where I can show off some of the work that I am proud to have made.',
        'technologies': [
            "Docker & Docker-Compose",
            "Django"
        ],
        'links': [
            { 'text': 'Demo', 'url': 'https://emwj.dev/' },
            { 'text': 'GitHub', 'url': 'https://github.com/emwjacobson/emwj.dev'}
        ]
    },
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
    {
        'image': 'https://i.imgur.com/K6mEpUM.png',
        'title': 'Pypc2',
        'description': 'For a while I was really into Project Cars 2, so I created a custom dashboard to be displayed while driving. It includes the car\'s current RPM, speed, and gear, as well as a meter showing when to shift, current throttle/braking, and g-forces applied to the car.',
        'technologies': [
            "Python",
            "Pygame"
        ],
        'links': [
            { 'text': 'GitHub', 'url': 'https://github.com/emwjacobson/pypc2'}
        ]
    },
]

def index(request):
    return render(request, 'app/index.html', {'projects': projects})

def about(request):
    return render(request, 'app/about.html')
