import { Text } from 'react-native';

const RepositoryItem = ({item}) => {
    return (
        <>
        <Text>Full name:  {item.fullName}</Text>
        <Text>Description:  {item.description}</Text>
        <Text>Language:  {item.language}</Text>
        <Text>Stars:  {item.stargazersCount}</Text>
        <Text>Forks:  {item.forksCount}</Text>
        <Text>Reviews:  {item.reviewCount}</Text>
        <Text>Rating:  {item.ratingAverage}</Text>
        </>
    )
}

// id: 'django.django',
// fullName: 'django/django',
// description: 'The Web framework for perfectionists with deadlines.',
// language: 'Python',
// forksCount: 21015,
// stargazersCount: 48496,
// ratingAverage: 73,
// reviewCount: 5,
// ownerAvatarUrl: 'https://avatars2.githu

export default RepositoryItem; 