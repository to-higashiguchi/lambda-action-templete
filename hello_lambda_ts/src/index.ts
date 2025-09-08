import { APIGatewayProxyHandler } from 'aws-lambda';

export const handler: APIGatewayProxyHandler = async (event, context) => {
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: 'hello from TypeScript!',
    }),
  };
};

// スクリプトが直接実行された場合にテストコードを呼び出す
if (require.main === module) {
  console.log("--- Running Local Test ---");
  // @ts-ignore
  handler({}, {}).then(result => {
    console.log(JSON.parse(result.body));
  });
  console.log("--- End of Local Test ---");
}