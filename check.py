import asyncio
import socks
from telethon import TelegramClient
from telethon.errors import UsernameInvalidError, FloodWaitError
from telethon.tl.functions.contacts import ResolveUsernameRequest

API_ID = 17349
API_HASH = "344583e45741c457fe1862106095a5eb"
PROXY = (socks.SOCKS5, "127.0.0.1", 10808)

async def check_username(client, username):
    try:
        result = await client(ResolveUsernameRequest(username))
        if result.users or result.chats:
            return "TAKEN ❌"
        else:
            return "FREE ✅"
    except UsernameInvalidError:
        return "INVALID ⚠️"
    except FloodWaitError as e:
        await asyncio.sleep(e.seconds)
        return await check_username(client, username)
    except Exception:
        return "FREE ✅"

async def main():
    async with TelegramClient("session", API_ID, API_HASH, proxy=PROXY) as client:
        print("Enter usernames (one per line). Empty line to start checking.\n")
        usernames = []
        while True:
            username = input("").strip().lstrip("@")
            if username == "":
                break
            usernames.append(username)

        if not usernames:
            print("No usernames entered.")
            return

        print(f"\n{'Username':<20} {'Status'}")
        print("-" * 35)
        for username in usernames:
            status = await check_username(client, username)
            print(f"@{username:<19} {status}")

asyncio.run(main())
