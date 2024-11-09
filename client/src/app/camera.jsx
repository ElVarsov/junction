import { StatusBar } from "expo-status-bar";
import { Text, View } from "react-native";

export default function CameraScreen() {
  return (
    <View className="pt-10 px-6">
      <Text className="text-primary font-bold text-4xl">Camera</Text>
      <StatusBar style="auto" />
    </View>
  );
}
