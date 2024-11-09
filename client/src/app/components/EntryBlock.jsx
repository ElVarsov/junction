import { Link } from "expo-router";
import { Linking, Pressable, Text, View } from "react-native";
import { Icon } from "react-native-elements";

export default function EntryBlock() {
  const styles = {
    date: "text-sm",
    entryName: "text-lg font-bold",
    location: "text-primary text-base",
    description: "text-base",
  };

  const openLink = () => {
    // Open the URL in the default browser
    const buildingAddressFormatted = buildingAddress.replace(/ /g, "+");
    Linking.openURL(
      `https://google.com/maps/place/${buildingAddressFormatted}`
    ).catch((err) => console.error("Failed to open URL: ", err));
  };

  return (
    <View className="p-4 bg-[#ffffff] border border-[#F0F0F0] rounded-lg">
      <Text className={styles.date}>Just now</Text>
      <Text className={styles.entryName}>
        [Equipment name] - [Equipment type]
      </Text>
      <Pressable onPress={openLink} className="flex flex-row items-center py-2">
        <Icon name="location-pin" color="#1450F5" />
        <Text className={styles.location}>Building address/location</Text>
      </Pressable>

      <Text className={styles.description}>
        location in building / serial number / model
      </Text>
    </View>
  );
}
