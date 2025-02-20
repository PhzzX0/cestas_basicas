from django.test import TestCase, Client
from django.urls import reverse
from .models import Instituicao, Doador, CestaBasica
from .forms import InstituicaoForm, DoadorForm, CestaBasicaForm

# Testes para os modelos
class ModelTests(TestCase):
    def test_criar_instituicao(self):
        """Testa a criação de uma instituição."""
        instituicao = Instituicao.objects.create(
            nome="Instituição Teste",
            endereco="Rua Teste, 123",
            telefone="123456789",
            email="teste@instituicao.com"
        )
        self.assertEqual(instituicao.nome, "Instituição Teste")
        self.assertEqual(instituicao.endereco, "Rua Teste, 123")

    def test_criar_doador(self):
        """Testa a criação de um doador."""
        doador = Doador.objects.create(
            nome="Doador Teste",
            endereco="Rua Teste, 456",
            telefone="987654321",
            email="teste@doador.com"
        )
        self.assertEqual(doador.nome, "Doador Teste")
        self.assertEqual(doador.email, "teste@doador.com")

    def test_criar_cesta_basica(self):
        """Testa a criação de uma cesta básica."""
        instituicao = Instituicao.objects.create(
            nome="Instituição Teste",
            endereco="Rua Teste, 123",
            telefone="123456789",
            email="teste@instituicao.com"
        )
        doador = Doador.objects.create(
            nome="Doador Teste",
            endereco="Rua Teste, 456",
            telefone="987654321",
            email="teste@doador.com"
        )
        cesta = CestaBasica.objects.create(
            descricao="Cesta Básica Teste",
            quantidade=10,
            doador=doador,
            instituicao=instituicao
        )
        self.assertEqual(cesta.descricao, "Cesta Básica Teste")
        self.assertEqual(cesta.quantidade, 10)
        self.assertEqual(cesta.doador.nome, "Doador Teste")
        self.assertEqual(cesta.instituicao.nome, "Instituição Teste")


# Testes para as views
class ViewTests(TestCase):
    def setUp(self):
        """Configuração inicial para os testes."""
        self.client = Client()
        self.instituicao = Instituicao.objects.create(
            nome="Instituição Teste",
            endereco="Rua Teste, 123",
            telefone="123456789",
            email="teste@instituicao.com"
        )
        self.doador = Doador.objects.create(
            nome="Doador Teste",
            endereco="Rua Teste, 456",
            telefone="987654321",
            email="teste@doador.com"
        )
        self.cesta = CestaBasica.objects.create(
            descricao="Cesta Básica Teste",
            quantidade=10,
            doador=self.doador,
            instituicao=self.instituicao
        )

    def test_lista_instituicoes(self):
        """Testa a view de lista de instituições."""
        response = self.client.get(reverse('lista_instituicoes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Instituição Teste")

    def test_lista_doadores(self):
        """Testa a view de lista de doadores."""
        response = self.client.get(reverse('lista_doadores'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Doador Teste")

    def test_lista_cestas(self):
        """Testa a view de lista de cestas básicas."""
        response = self.client.get(reverse('lista_cestas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cesta Básica Teste")


# Testes para os formulários
class FormTests(TestCase):
    def test_instituicao_form_valido(self):
        """Testa se o formulário de instituição é válido."""
        form_data = {
            'nome': 'Instituição Teste',
            'endereco': 'Rua Teste, 123',
            'telefone': '123456789',
            'email': 'teste@instituicao.com'
        }
        form = InstituicaoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_doador_form_valido(self):
        """Testa se o formulário de doador é válido."""
        form_data = {
            'nome': 'Doador Teste',
            'endereco': 'Rua Teste, 456',
            'telefone': '987654321',
            'email': 'teste@doador.com'
        }
        form = DoadorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cesta_basica_form_valido(self):
        """Testa se o formulário de cesta básica é válido."""
        instituicao = Instituicao.objects.create(
            nome="Instituição Teste",
            endereco="Rua Teste, 123",
            telefone="123456789",
            email="teste@instituicao.com"
        )
        doador = Doador.objects.create(
            nome="Doador Teste",
            endereco="Rua Teste, 456",
            telefone="987654321",
            email="teste@doador.com"
        )
        form_data = {
            'descricao': 'Cesta Básica Teste',
            'quantidade': 10,
            'doador': doador.id,
            'instituicao': instituicao.id
        }
        form = CestaBasicaForm(data=form_data)
        self.assertTrue(form.is_valid())