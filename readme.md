Test task for LeadsDoIt

To start project run "docker-compose up --build -d"



Api endpoint:
http://0.0.0.0:8000/temperature/?day=2024-01-23

Headers (can be edited in .env file) :
{
    x-token: TSpDX?y8o-nNPtDtUw=2aL3OAsi?bBdA
}

Params
{
    day: 2024-01-23
}

Response 
{
    {
    "status": 1,
    "city": "Kyiv",
    "day": "2024-01-23",
    "temperatures": [
        {
            "time": "16:39:48",
            "temperature": -0.3
        }
        ]
    }
}

Weather API trial period ends 06.02, so if you check it after, let me know to updated token.