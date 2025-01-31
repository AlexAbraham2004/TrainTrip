import { Image, Text, View, StyleSheet, TouchableOpacity} from "react-native";
import Colors from '../constant/Colors'
import { useRouter } from 'expo-router';

export default function Index() {

  const router = useRouter(); 

  return (
    <View
      style={{
        flex: 1,
        backgroundColor: Colors.WHITE
      }}
    >
      <Image source={require('./../assets/images/landing.png')}
      style={{
        width: '95%',
        alignSelf: 'center',
        height: 300,
        marginTop: 20, 
        borderRadius: 30
      }}
      />
      <View style={{
        marginTop: 15, 
        marginLeft: 10, 
        marginRight: 10, 
        padding:25, 
        backgroundColor: Colors.PRIMARY,
        height: '100%',
        borderTopLeftRadius: 35, 
        borderTopRightRadius: 35
      }}>
        <Text style={{
          fontSize: 30,
          fontWeight: 'bold', 
          textAlign: 'center', 
          color: Colors.WHITE, 
          fontFamily:'outfit-bold'
        }}>Welcome to Train Trip!</Text>

        <Text style={{
          fontSize: 20,
          color: Colors.WHITE,
          marginTop: 20, 
          textAlign: 'center',
          fontFamily:'outfit'
        }}>Stay ahead of your commute with real-time LIRR updates! Get instant notifications on delays, track changes, train timings, and service alerts—all in one seamless app.</Text>
      
      <TouchableOpacity style={styles.button}
        onPress={()=>router.push('/auth/signUp')}
      >
        <Text style={[styles.buttonText, {color: Colors.PRIMARY}]}>Get Started</Text>
      </TouchableOpacity>

      <TouchableOpacity 
        onPress={() => router.push('/auth/signIn')} 
        style={[styles.button, {
          backgroundColor: Colors.PRIMARY,
          borderWidth: 1, 
          borderColor: Colors.WHITE
        }]}>
        <Text style={[styles.buttonText, {color: Colors.WHITE}]}>Already Have an Account?</Text>
      </TouchableOpacity>

      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  button: {
    padding: 15, 
    backgroundColor: Colors.WHITE,
    marginTop: 20, 
    borderRadius: 10
  }, 

  buttonText: {
    textAlign: 'center', 
    fontSize: 18,
    fontFamily: 'outfit-semibold'
  }
})