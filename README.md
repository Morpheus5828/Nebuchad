# Welcome to Nebuchad

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWh0ZXZrZXcwcWVtOW1nemx4bXdzY21xN2UyMmtzcTBxNHluNHNtaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11e0gEWxYoSYTK/giphy.gif"></img>

# Send automatic email
1. Create <a href="https://support.google.com/accounts/answer/185833?hl=fr">application password</a><br>
2. Create a json file like this:
```json
{
    "mail": {
        "password": "MAIL@gmail.com",
        "user": "PASSWORD"
    }
}
```
3. And then send you message automatically:
```shell
python nebuchad/phoneMessage.py -t "[Alert]" -m "Process over" -d "marius.thorre@etu.univ-amu.fr"-path "C:/Users/thorr/OneDrive/Bureau/perso.json"
```

