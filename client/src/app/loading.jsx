import { Image, Text } from "react-native-elements";
import { View } from "react-native";
import { StatusBar } from "expo-status-bar";
import TypeWriter from "react-native-typewriter";

export default function loading() {
  const loadingGif = require("../../assets/loading.gif");
  return (
    <View className="w-full h-full items-center justify-center">
      <Image
        source={loadingGif}
        style={{ width: 90, height: 90 }} // Adjust size as needed
      />
      <TypeWriter
        typing={1}
        maxDelay={50}
        minDelay={10}
        fixed={true}
        style={{ fontSize: 20, color: "#000000" }}
      >
        Analyzing the image...
      </TypeWriter>
      <StatusBar style="dark" />
    </View>
  );
}
