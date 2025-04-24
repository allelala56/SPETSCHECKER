import asyncio
from checker.client import run_checker
from checker.config import load_config
from checker.proxy import load_proxies
from checker.parser import load_combos

async def main():
    config = load_config()
    combos = load_combos("data/combo.txt")
    proxies = load_proxies("data/proxies.txt")

    print(f"[+] URL ciblée : {config['TARGET_URL']}")
    print(f"[+] Chargement de {len(combos)} combos.")
    print(f"[+] Chargement de {len(proxies)} proxies.
")

    await run_checker(combos, proxies, config)

if __name__ == "__main__":
    asyncio.run(main())
