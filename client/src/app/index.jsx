import * as FileSystem from "expo-file-system";
import { Link, useRouter } from "expo-router";
import * as Location from "expo-location";
import { StatusBar } from "expo-status-bar";
import { useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import EntryBlock from "./components/EntryBlock";
import * as ImagePicker from "expo-image-picker";

import Icon from "react-native-vector-icons/MaterialCommunityIcons";

export default function Page() {
  return (
    <View className="pt-20 flex flex-1">
      <Content />
    </View>
  );
}

function Content() {
  const router = useRouter();
  const [image, setImage] = useState();

  async function uploadImage() {
    try {
      // Request camera permissions
      await ImagePicker.requestCameraPermissionsAsync();

      // Request location permissions
      const { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== "granted") {
        alert("Location permission not granted");
        return;
      }

      // Capture photo
      let result = await ImagePicker.launchCameraAsync({
        cameraType: ImagePicker.CameraType.back,
        allowsEditing: false,
      });

      if (!result.canceled) {
        // Get current location
        router.replace("/loading");
        const location = await Location.getCurrentPositionAsync({});

        // Save and process image
        await saveImage(result.assets[0].uri, location);
      }
    } catch (error) {
      alert("Error uploading image: " + error.message);
    }
  }

  const saveImage = async (imageUri, location) => {
    try {
      // // Convert image to base64
      // const base64Image = await FileSystem.readAsStringAsync(imageUri, {
      //   encoding: FileSystem.EncodingType.Base64,
      // });

      // // Send base64 image and location to the server
      // await sendImageToServer(base64Image, location);
      router.replace("/imageData");
    } catch (error) {
      console.error("Error saving image:", error);
    }
  };

  const sendImageToServer = async (base64Image, location) => {
    try {
      const response = await fetch("http://10.87.0.190:5000/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          image: base64Image,
          location: {
            latitude: location.coords.latitude,
            longitude: location.coords.longitude,
          },
        }),
      });

      const data = await response.json();
      console.log("Server response:", data);
      router.replace("/imageData");
    } catch (error) {
      console.error("Error sending image to server:", error);
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
      <Pressable
        onPress={() => uploadImage()}
        className="absolute bottom-20 left-8 right-8 bg-primary items-center rounded-lg py-4 text-white flex flex-row justify-center gap-4"
      >
        <Text className="text-[#ffffff] font-semibold text-2xl">Scan</Text>
        <Icon name="cube-scan" size={25} color="#ffffff" />
      </Pressable>

      <StatusBar style="dark" />
    </View>
  );
}
