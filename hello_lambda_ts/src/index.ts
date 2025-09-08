import { APIGatewayProxyHandler } from 'aws-lambda';
import axios from 'axios';

// PokeAPI のレスポンス型定義
interface PokemonResponse {
  name: string;
  id: number;
}

export const handler: APIGatewayProxyHandler = async (event, context) => {
    const response = await axios.get<PokemonResponse>('https://pokeapi.co/api/v2/pokemon/25');
    return {
        statusCode: 200,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
        message: response.data.name,
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