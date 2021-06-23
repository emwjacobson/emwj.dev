from django.shortcuts import render
from django.templatetags.static import static

projects = [
    {
        'image': static('r510.jpg'),
        'title': 'Self-hosted Homelab',
        'description': 'I run a Dell R510 with dual 6C/12T Xeon X5650 processors and 112 GB of Memory. \
            I have Proxmox installed and use it to virtualize many servers. Some services I run are: \
            PiHole for DNS Adblocking, an NFS for file storage, Plex for home media streaming, a machine \
            for running Docker images, NextCloud, and Nginx as a reverse proxy.',
        'technologies': [
            "Proxmox (Hypervisor)",
            "Nginx (Reverse Proxy)",
            "Nextcloud",
            "Docker",
            "Plex"
        ],
        'links': []
    },
    {
        'image': static('mchost.jpg'),
        'title': 'MCHoster',
        'description': 'This project aims to create on-demand Minecraft Servers. I used Docker to streamline \
            development and make the creation/destruction of servers extremely easy. I used Django as the \
            Frontend as I wanted to learn more about it. I later expanded on this project to use Docker Swarm, \
            allowing for High Availability and distribution of the load across multiple servers.',
        'technologies': [
            "Docker (Compose & Swarm)",
            "Django"
        ],
        'links': [
            { 'text': 'Demo', 'url': 'https://mc.emwj.dev/' },
            { 'text': 'GitHub', 'url': 'https://github.com/emwjacobson/MCHoster' }
        ]
    },
    {
        'image': static('site.jpg'),
        'title': 'This Website!',
        'description': 'With a bit of downtime between my Summer Research Program and my first Quarter at the University of California, Riverside, I decided it was time to make myself a portfolio website. Here I can show off some of the work that I am proud to have made.',
        'technologies': [
            "Docker & Docker Compose",
            "Django"
        ],
        'links': [
            { 'text': 'Demo', 'url': 'https://emwj.dev/' },
            { 'text': 'GitHub', 'url': 'https://github.com/emwjacobson/emwj.dev'}
        ]
    },
    {
        'image': static('pc2.jpg'),
        'title': 'Pypc2',
        'description': 'For a while, I was really into Project Cars 2, so I created a custom dashboard to be displayed while driving. It uses data from the game to display the car\'s current RPM, speed, and gear. It also has a meter showing when to shift, current throttle/braking, and g-forces applied to the car.',
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

def research(request):
    return render(request, 'app/research.html')

def education(request):
    return render(request, 'app/education.html')
