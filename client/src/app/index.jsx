import { Link } from "expo-router";
import { StatusBar } from "expo-status-bar";
import React, { useState } from "react";
import { Pressable, Text, View } from "react-native";
import EntryBlock from "./components/EntryBlock";
import * as ImagePicker from "expo-image-picker";

export default function Page() {
  return (
    <View className="pt-20 px-6 flex flex-1">
      <Content />
    </View>
  );
}

function Content() {
  const [image, setImage] = useState();
  console.log(image);

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
    <View className="h-full relative">
      <Text className="text-primary font-bold text-4xl">Last entries</Text>
      <EntryBlock />
      <Link href="/imageData" asChild>
        <Pressable
          onPress={() => uploadImage()}
          className="absolute bottom-20 left-8 right-8 bg-primary items-center rounded-lg py-4 text-white"
        >
          <Text className="text-[#ffffff] font-semibold text-2xl">
            Add entry
          </Text>
        </Pressable>
      </Link>

      <StatusBar style="auto" />
    </View>
  );
}
