import { Link } from "expo-router";
import { StatusBar } from "expo-status-bar";
import { Linking, Pressable, Text, View } from "react-native";
import { Icon } from "react-native-elements";

export default function EntryBlock() {
  // const openLink = () => {
  //   // Open the URL in the default browser
  //   const buildingAddressFormatted = buildingAddress.replace(/ /g, "+");
  //   Linking.openURL(
  //     `https://google.com/maps/place/${buildingAddressFormatted}`
  //   ).catch((err) => console.error("Failed to open URL: ", err));
  // };

  return (
    <View className="p-4 bg-[#ffffff] border border-[#F0F0F0] rounded-lg">
      <Text className="text-base font-medium text-[#8a8a8a]">Just now</Text>
      <Text className="text-xl mb-2 font-bold">
        [Equipment name] - [Equipment type]
      </Text>
      {/* <Pressable onPress={openLink} className="flex flex-row items-center py-2">
        <Icon name="location-pin" color="#1450F5" />
        <Text className="text-primary text-base">Building address/location</Text>
      </Pressable> */}

      <Text className="text-base">
        location in building / serial number / model
      </Text>
      <StatusBar style="dark" />
    </View>
  );
}
