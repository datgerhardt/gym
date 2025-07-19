import Constants from 'expo-constants';
import { Text, View, StyleSheet,  Pressable, Alert} from "react-native";

import RepositoryList from './RepositoryList';


const styles = StyleSheet.create ({
    container: {
        marignTop: Constants.statusBarHeight,
        flexGrow: 1,
        flexShrink: 1,
    },

});


// const styles = StyleSheet.create({
//       container: {
//         flex: 1,
//         backgroundColor: '#fff',
//         alignItems: 'center',
//         justifyContent: 'center',
//       },
//     });

const Main = () => {
    return (
        <View style={styles.container}>
            <Text> Rate Respository Application</Text>
            <RepositoryList/>
            <Text> Hoo </Text>
        </View>
    )
}

// const HelloWorld = props => {
//     return<View><Text>Hello World</Text></View>;
// }
// // export default HelloWorld;

// const PressableText = props => {
//   return (
//     <Pressable onPress={() => Alert.alert("You pressed the the text")}>
//       <Text>You can press here</Text>
//     </Pressable>
//   )
// }


export default Main;