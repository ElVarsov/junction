import { Text, View } from "react-native";
// import { Icon } from "react-native-elements";

export default function EntryBlock() {
  const styles = {
    date: "text-sm",
    entryName: "text-lg font-bold",
    location: "text-primary text-base",
    description: "text-base",
  };
  return (
    <View className="py-4">
      <Text className={styles.date}>Just now</Text>
      <Text className={styles.entryName}>
        [Equipment name] - [Equipment type]
      </Text>
      <View className="flex flex-row items-center py-2">
        {/* <Icon name="location-pin" color="primary" /> */}
        <Text className={styles.location}>Building address/location</Text>
      </View>

      <Text className={styles.description}>
        location in building / serial number / model
      </Text>
    </View>
  );
}
