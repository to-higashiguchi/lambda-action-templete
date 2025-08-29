import json
import requests


def lambda_handler(event, context):
    """
    PokeAPIを呼び出してポケモンの情報を取得するLambdaハンドラ関数
    """
    pokemon_id = "25"  # ピカチュウのID
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    try:
        # PokeAPIにGETリクエストを送信
        response = requests.get(api_url)

        # レスポンスが成功したかチェック (ステータスコード 200)
        response.raise_for_status()

        # レスポンスのJSONをパース
        data = response.json()
        pokemon_name = data.get("name")

        # 成功レスポンスを返す
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {
                    "message": "Successfully fetched data from PokeAPI!",
                    "pokemonName": pokemon_name,
                }
            ),
        }

    except requests.exceptions.RequestException as e:
        # API呼び出しでエラーが発生した場合
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Failed to fetch data from PokeAPI."}),
        }


# --- ローカルテスト用のコードを追加 ---
if __name__ == "__main__":
    # Lambda関数を直接呼び出し、結果をコンソールに表示する
    # eventとcontext引数にはNoneや空の辞書{}を渡す
    print("--- Running Local Test ---")
    result = lambda_handler({}, None)

    # 見やすいように整形して出力
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("--- End of Local Test ---")
