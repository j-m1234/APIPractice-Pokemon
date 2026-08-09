import requests
import PokeEndPoints
import json

def get_pokemon_data(endpoint, NameID):
    url = f"https://pokeapi.co/api/v2/{endpoint}/{NameID}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response.status_code
    



if __name__ == "__main__":
    print("\nWelcome to the Pokemon API Practice!\n")
    while True:
        print("\nAvailable categories:")
        for key in PokeEndPoints.dictionary:
            print(key)
        inputEP = input("\nSelect one of the above options: ").strip().lower()
        if inputEP in PokeEndPoints.dictionary.keys():
            print(f"\nYou selected: {inputEP}")
            print("\nAvailable endpoints:")
            for endpoint in PokeEndPoints.dictionary[inputEP]:
                print(endpoint)
            inputEndpoint = input("\nSelect one of the above endpoints: ").strip().lower()
            if inputEndpoint in PokeEndPoints.dictionary[inputEP]:
                print(f"You selected: {inputEndpoint}")
                inputNameID = input("\nEnter the desired name or ID for your selection: ").strip().lower()
                data = get_pokemon_data(inputEndpoint, inputNameID)
                if isinstance(data, dict)== True:
                    print(json.dumps(data, indent=4))
                else:
                    print(f"\nError: Received status code {data} from the API.")
        inputContinue = input("\nIf you want to continue, say 'yes'.  Anything else will end the interaction.\nWhat do you say? ").strip().lower()
        if inputContinue != "yes":
            print("\nThank you for using the Pokemon API Practice! Goodbye!\n")
            break