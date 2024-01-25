def command(input_value, thread_userid=None):
    config = {
        "name": "elians",
        "version": "1.0.0",
        "description": "Developer.",
        "credits": "𝙀𝙇.𝙄𝘼𝙉𝙎 𝙍𝙀𝙏𝙄𝙍𝙊 𝙎𝙊𝙏𝙀𝙍𝙊",
        "cooldown": "1"
    }
    if input_value == "__config__":
        return config
    elif input_value.startswith(config['name'] + ' ') or input_value == config['name']: 
    	return {'messages': ["DEVELOPED BY MAHIRO CHAN"], 'image': ['commands/images/onimai-oniichan-wa-oshimai.gif']}
    else:
        return {'messages': [f"Default option in {config['name']}: {config['description']}"]}
