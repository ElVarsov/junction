import { StatusBar } from "expo-status-bar";
import { Text, View } from "react-native";

export default function CameraScreen() {
  return (
    <View className="">
      <Text className="text-primary font-bold text-4xl">Camera</Text>
      <StatusBar style="auto" />
    </View>
  );
}
