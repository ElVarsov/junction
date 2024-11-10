import { Link, router, useLocalSearchParams } from "expo-router";
import { StatusBar } from "expo-status-bar";
import { useEffect, useRef, useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";
import Icon from "react-native-vector-icons/MaterialCommunityIcons";

export default function App() {
  const [formData, setFormData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://10.87.0.190:5000/fetch", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });
        if (response.ok) {
          const result = await response.json();
          console.log(result);
          const { id, upload_time, additional_data, ...detailsWithoutId } =
            result.details;
          setFormData(detailsWithoutId);
        } else {
          console.error("Failed to get image data:", response.status);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  function formatKey(key) {
    return key
      .split("_") // Split by underscore
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1)) // Capitalize each word
      .join(" "); // Join with a space
  }

  const handleInputChange = (key, newValue) => {
    setFormData((prevData) => ({
      ...prevData,
      [key]: newValue,
    }));
  };

  return (
    <View className="relative h-full pt-20">
      <View className="px-4 pb-6">
        <Link href="/" className="text-xl text-primary">
          <Text>Back</Text>
        </Link>
        <Text className="text-4xl font-semibold mt-8">Gathered data</Text>
      </View>
      <View className="pb-32">
        <ScrollView className="bg-[#fafafa] border-t-2 border-[#FAFAFA] px-4 mb-36">
          <View className="pb-24">
            {Object.entries(formData).map(([key, value]) => (
              <View className="mt-4" key={key}>
                <Text className="text-lg mb-2 font-semibold">
                  {formatKey(key)}
                </Text>
                <TextInput
                  className="bg-[#ffffff] border-2 border-[#c6c6c6] text-[#000000] p-4 rounded-md"
                  onChangeText={(newValue) => handleInputChange(key, newValue)}
                  value={value}
                  placeholder={"Enter"}
                  placeholderTextColor="#999999"
                />
              </View>
            ))}
          </View>
        </ScrollView>
      </View>

      <Pressable className="absolute bottom-16 left-8 right-8 bg-primary p-4 flex flex-row justify-center gap-4 items-center rounded-lg">
        <Text className="text-[#ffffff] font-medium text-xl">Add to BIM</Text>
        <Icon name="database-plus-outline" color="#ffffff" size="25" />
      </Pressable>
      <StatusBar style="dark" />
    </View>
  );
}
