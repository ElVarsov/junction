import { Link } from "expo-router";
import { useEffect, useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";
import { Image } from "react-native-elements";

export default function App() {
  const [fields, setFields] = useState(["Equipment name", "Model", "Age"]);
  const [formData, setFormData] = useState({});

  // useEffect(() => {
  //   // Fetch data from the server when component mounts
  //   fetch("http://YOUR_FLASK_SERVER_URL/get_equipment_data")
  //     .then((response) => response.json())
  //     .then((data) => {
  //       setFields(Object.keys(data)); // Set field names dynamically
  //       setFormData(data); // Set initial values from the server data
  //     })
  //     .catch((error) => {
  //       console.error("Error fetching data from server:", error);
  //     });
  // }, []);

  // const handleInputChange = (key, value) => {
  //   setFormData((prevData) => ({ ...prevData, [key]: value }));
  // };

  return (
    <View className="relative h-full pt-20">
      <View className="px-4 pb-6">
        <Link href="/" className="text-xl text-primary">
          <Text>Back</Text>
        </Link>
        <Text className="text-4xl font-semibold mt-8">Gathered data</Text>
      </View>

      <ScrollView className="bg-[#fafafa] border-t-2 border-[#FAFAFA] px-4">
        {fields.map((field) => (
          <View className="mt-4" key={field}>
            <Text className="text-lg mb-2 font-semibold">
              {field.replace(/_/g, " ").toUpperCase()}
            </Text>
            <TextInput
              className="bg-[#ffffff] border-2 border-[#c6c6c6] text-[#000000] p-4 rounded-md"
              value={formData[field]?.toString() || ""}
              onChangeText={(value) => handleInputChange(field, value)}
              placeholder={`Enter ${field}`}
              placeholderTextColor="#999999"
            />
          </View>
        ))}
      </ScrollView>
      <Pressable className="absolute bottom-20 left-8 right-8 bg-primary p-4 items-center rounded-lg">
        <Text className="text-[#f5c4c4] font-medium text-xl">Add to BIM</Text>
      </Pressable>
    </View>
  );
}
