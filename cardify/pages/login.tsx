import React, { useState} from "react";
import { Text, View, Button, StyleSheet, Alert } from "react-native";
import {authorize, AuthorizeResult} from 'react-native-app-auth';
import AsyncStorage from '@react-native-async-storage/async-storage';

const config = {
    issuer: 'https://accounts.google.com',
    clientId: '469763989203-sc3hbgi1vjaulbrikqvpplvkiqkjo9uk.apps.googleusercontent.com',
    redirectUrl: 'com.googleusercontent.apps.469763989203-sc3hbgi1vjaulbrikqvpplvkiqkjo9uk:/oauthredirect',
    scopes: ['openid', 'profile', 'email']
  };

const LoginPage = () => {
    const [isLoggingIn, setIsLoggingIn] = useState(false);

    const handleLogin = async () => {
        try {
            setIsLoggingIn(true);

            const authState: AuthorizeResult = await authorize(config);
            await AsyncStorage.setItem('accessToken', authState.accessToken);

            Alert.alert('Login Successful!', `Welcome ${authState.tokenAdditionalParameters?.name}`);
            } catch (error) {
            if (error instanceof Error) {
                Alert.alert('Login Failed', error.message);
            } else {
                Alert.alert('Login Failed', 'An unknown error occurred.');
            }
        }
        finally {
            setIsLoggingIn(false);
        }
}; 

return (
    <View style={styles.container}>
    <Text style={styles.title}>Welcome to Cardify!</Text>
    <Button title="Login with Google" onPress={handleLogin} disabled={isLoggingIn} />
    </View>
);
};

const styles = StyleSheet.create({
container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f8f9fa',
},
title: {
    fontSize: 24,
    marginBottom: 20,
},
});
export default LoginPage