import json


def lambda_handler(event, context):
    """
    AWS Lambdaで実行されるメインの関数。
    """
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello_lambda!",
            }
        ),
    }


def main():
    """
    ローカルでのテスト実行用のメイン関数。
    """
    # Lambda関数に渡すeventとcontextのダミーデータを作成
    # event: Lambda関数への入力データ。API Gatewayからのリクエストなどを想定
    mock_event = {}

    # context: Lambdaの実行環境に関する情報。通常、ローカルテストでは多くを必要としない
    mock_context = {}

    # lambda_handlerを直接呼び出し、結果を表示
    response = lambda_handler(mock_event, mock_context)
    print("Lambda function response:")
    print(json.dumps(response, indent=4))


# スクリプトが直接実行された場合にmain()を呼び出す
if __name__ == "__main__":
    main()
