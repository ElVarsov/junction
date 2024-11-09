import { View } from "react-native";
import { verifyInstallation } from "nativewind";

export default function App() {
  verifyInstallation();
  return <View className="pt-20 px-6"></View>;
}
