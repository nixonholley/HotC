import React from "react";
import { Text, View, TouchableOpacity, StyleSheet } from "react-native";
import { StackNavigationProp } from '@react-navigation/stack';

// Define the stack navigator type
type RootStackParamList = {
  Home: undefined;
  Login: undefined;
};

type HomePageProps = {
  navigation: StackNavigationProp<RootStackParamList, 'Home'>;
};

const HomePage: React.FC<HomePageProps> = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Welcome to Cardify</Text>
      <Text style={styles.subHeader}>Card Scanner and Value Evaluator</Text>
      
      <TouchableOpacity 
        style={styles.button} 
        onPress={() => navigation.navigate('Login')}
      >
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f5f5f5",
    padding: 16,
  },
  header: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#333",
  },
  subHeader: {
    fontSize: 18,
    color: "#666",
    marginTop: 8,
  },
  button: {
    marginTop: 16,
    paddingVertical: 12,
    paddingHorizontal: 32,
    backgroundColor: "#3b82f6",
    borderRadius: 8,
  },
  buttonText: {
    fontSize: 16,
    color: "#fff",
    textAlign: "center",
  },
});

export default HomePage;
