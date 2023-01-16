import pytest
from pytest import mark

from codigo.bytebank import Funcionario


# Given-When-Then é uma metodologia ágil para desenvolvimento de testes
class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Guilherme_Mendes_deve_retornar_Mendes(self):
        entrada = "  Guilherme Mendes   "  # Given
        esperado = "Mendes"

        guilherme = Funcionario(entrada, "21/05/1999", 1500)
        resultado = guilherme.sobrenome()  # When

        assert resultado == esperado  # Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/1999', entrada_salario)
        funcionario_teste.decrescimo_salario()  # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/1999', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salrio = 1000000  # given

            funcionario_teste = Funcionario('teste', '11/11/1999', entrada_salrio)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then
