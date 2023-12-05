import requests

def get_insult():
    try:
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        if response.status_code == 200:
            insult_data = response.json()
            return f"{insult_data["insult"]}"
        else:
            return "Failed to fetch a quote."
    except Exception as e:
        return f"Error: {e}"
    
print(f"""\nGet insulted:\n {get_insult()}\n\n\n
          $$$$$$
         $$____$$
         $$$__$$$
         $$_$$_$$
         $$____$$
         $$____$$
         $$____$$
         $$____$$$$$$$
   $$$$$$$$____$$____$$
 $$$$$___$$____$$____$$$$$$
$$$_$$___$$____$$____$$___$$
$$__$$___$$____$$____$$___$$
$$__$$___$$____$$____$$___$$
$$__$$___$$____$$___$$$___$$
$$__$$___$$____$$____$____$$
$$____$$$__$$$$__$$$$___$_$$
$$________________________$$
 $$_______________________$$
 $$$_____________________$$
  $$$$_________________$$$
    $$_________________$
    $$$_______________$$
""")

input()