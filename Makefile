package:
	# Cria o pacote no formato tar.gz e insere no diretório dist
	python3 setup.py sdist bdist_wheel

install:
	# Instala o pacote no formato tar.gz
	pip3 install ./dist/vwapp-eda-0.2.0.tar.gz

uninstall:
	# Desistalar o pacote tar.gz
	pip3 uninstall vwapp-eda
	rm -rf ./build ./dist ./vwapp_eda.egg-info

clean:
	# Limpa a build
	rm -rf ./build ./dist ./{{cookiecutter.package|replace('-', '_')}}.egg-info

pypi_test:
	# Enviando o pacote para o PyPI Test
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pypi:
	# Enviando o pacote para o PyPI Live
	twine upload dist/*

flake8:
	# Roda a folha de estilo.
	flake8
