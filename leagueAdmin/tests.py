from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Players, Games

# Create your tests here.
class ViewsTestCase(TestCase):
    
    # Creating database for tests
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.player = Players.objects.create(name='John', surname='Doe', ranking=1330)
        self.game = Games.objects.create(players='John Doe', result='1:0')

    #----------------------------------------------------------------------#
    # Test that verifies if the page returns a valid response code (200)
    # and if the correct template is used
    #----------------------------------------------------------------------#
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html/')
        self.assertIn('all_p', response.context)
        self.assertIn('all_g', response.context)
        
    def test_games_view(self):
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games.html/')
        self.assertIn('all', response.context)
        
    def test_players_view(self):
        response = self.client.get(reverse('players'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'players.html/')
        self.assertIn('all', response.context)
        
    def test_log_in_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        
    #----------------------------------------------------------------------#
    # Test that checks whether a POST request will be made 
    # and checks CRUD operations on the test database
    #----------------------------------------------------------------------#   
    def test_player_add_view(self):
        response = self.client.post(reverse('player_add'), {'name': 'Jane', 'surname': 'Smith', 'ranking': 3})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player_add.html')
        self.assertTrue(Players.objects.filter(name='Jane', surname='Smith', ranking=3).exists())

    def test_player_delete_view(self):
        response = self.client.post(reverse('player_delete'), {'ID': self.player.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player_delete.html')
        self.assertFalse(Players.objects.filter(id=self.player.id).exists())

    def test_player_update_view(self):
        response = self.client.post(reverse('player_update'), {'ID': self.player.id, 'ranking': 7})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'player_update.html')
        self.player.refresh_from_db()
        self.assertEqual(self.player.ranking, 7)

    def test_game_add_view(self):
        response = self.client.post(reverse('game_add'), {'players': 'Jane Smith', 'result': '1:1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_add.html')
        self.assertTrue(Games.objects.filter(players='Jane Smith', result='1:1').exists())

    def test_game_delete_view(self):
        response = self.client.post(reverse('game_delete'), {'ID': self.game.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_delete.html')
        self.assertFalse(Games.objects.filter(id=self.game.id).exists())

    def test_game_update_view(self):
        response = self.client.post(reverse('game_update'), {'ID': self.game.id, 'result': '0:1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_update.html')
        self.game.refresh_from_db()
        self.assertEqual(self.game.result, '0:1')