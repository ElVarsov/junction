import { Link } from "expo-router";
import { StatusBar } from "expo-status-bar";
import { Pressable, Text, View } from "react-native";
import EntryBlock from "./components/EntryBlock";

export default function HomeScreen() {
  return (
    <View className="h-full relative pt-20">
      <Text className="text-primary font-bold text-4xl">Last entries</Text>
      <Link href="/camera">Click</Link>
      <EntryBlock />
      <Pressable className="absolute bottom-20 left-8 right-8 bg-primary items-center rounded-lg py-4 text-white">
        <Text className="text-[#ffffff] font-semibold text-2xl">Add entry</Text>
      </Pressable>
      <StatusBar style="auto" />
    </View>
  );
}