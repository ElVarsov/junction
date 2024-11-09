import { Link } from "expo-router";
import { StatusBar } from "expo-status-bar";
import React, { useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import EntryBlock from "./components/EntryBlock";
import * as ImagePicker from "expo-image-picker";

export default function Page() {
  return (
    <View className="pt-20 flex flex-1">
      <Content />
    </View>
  );
}

function Content() {
  const [image, setImage] = useState();

  const uploadImage = async () => {
    try {
      await ImagePicker.requestCameraPermissionsAsync();
      let result = await ImagePicker.launchCameraAsync({
        cameraType: ImagePicker.CameraType.back,
        allowsEditing: false,
      });

      if (!result.canceled) {
        // save image
        await saveImage(result.assets[0].uri);
      }
    } catch (error) {
      alert("Error uploading image: " + error.message);
    }
  };

  const saveImage = async (image) => {
    try {
      setImage(image);
    } catch (error) {
      throw error;
    }
  };

  return (
    <View className="h-full relative ">
      <View className="px-4">
        <Text className="text-primary font-bold text-4xl mb-8 ">Servisync</Text>
      </View>
      <ScrollView className="bg-[#fafafa] border-t border-[#f0f0f0] h-full pt-4">
        <View className="px-4">
          <Text className="text-black font-bold text-2xl mb-6">
            Last entries
          </Text>

          <EntryBlock />
        </View>
      </ScrollView>
      <Link href="/imageData" asChild>
        <Pressable
          onPress={() => uploadImage()}
          className="absolute bottom-20 left-8 right-8 bg-primary items-center rounded-lg py-4 text-white"
        >
          <Text className="text-[#ffffff] font-semibold text-2xl">Scan</Text>
        </Pressable>
      </Link>

      <StatusBar style="auto" />
    </View>
  );
}
