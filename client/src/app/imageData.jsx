import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function App() {
  return (
    <View className="pt-20 px-6">
      <Link href="/">
        <Text>Back</Text>
      </Link>
    </View>
  );
}
