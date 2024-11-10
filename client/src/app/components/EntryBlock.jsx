import { Link } from "expo-router";
import { StatusBar } from "expo-status-bar";
import { Linking, Pressable, Text, View } from "react-native";
import { Icon } from "react-native-elements";
import relativeTime from "dayjs/plugin/relativeTime";
import dayjs from "dayjs";

dayjs.extend(relativeTime);
function RelativeTime({ dateString }) {
  const relativeTime = dayjs(dateString).add(-2, "hour").fromNow();

  return <Text>{relativeTime}</Text>;
}

export default function EntryBlock({ entry }) {
  const openLink = () => {
    // Open the URL in the default browser
    const buildingAddressFormatted = entry.building_address.replace(/ /g, "+");
    Linking.openURL(
      `https://google.com/maps/place/${buildingAddressFormatted}`
    ).catch((err) => console.error("Failed to open URL: ", err));
  };

  return (
    <View className="p-4 bg-[#ffffff] border border-[#F0F0F0] rounded-lg mb-2">
      <Text className="text-base font-medium text-[#8a8a8a]">
        <RelativeTime dateString={entry.upload_time} />
      </Text>
      <Text className="text-xl font-bold">
        {entry.equipment_name || "[Equipment name]"}
      </Text>
      <Pressable onPress={openLink} className="flex flex-row items-center py-2">
        <Icon name="location-pin" color="#1450F5" size={20} />
        <Text className="text-primary text-base">
          {entry.building_address || "[Location]"}
        </Text>
      </Pressable>

      {/* <Text className="text-base">{entry.equipment_type}</Text> */}
      <StatusBar style="dark" />
    </View>
  );
}
