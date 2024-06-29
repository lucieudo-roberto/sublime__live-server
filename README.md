

# Plugin web-live para Sublime Text 3

## Visão Geral

web-live é um plugin para o Sublime Text 3 que permite iniciar um servidor de desenvolvimento local com recarregamento automático. Compatível com Linux e Windows, ele proporciona uma experiência de desenvolvimento fluida e eficiente.

## Funcionalidades

- **Recarregamento Automático**: Atualiza automaticamente o navegador ao salvar arquivos.
- **Compatibilidade**: Suporte para Linux e Windows.
- **Configuração Personalizável**: Permite definir o host e a porta através das configurações.
- **Comandos Simples**: Inicie e pare o servidor diretamente do Sublime Text.

## Requisitos

- **Node.js**: Certifique-se de ter o Node.js instalado.
- **live-server**: Deve ser instalado globalmente via npm.

  ```bash
  npm install -g live-server
  ```

- **Específico para Windows**: Certifique-se de que o `live-server` esteja no PATH do sistema.

## Instalação

1. Clone este repositório no diretório `Packages` do Sublime Text.
2. Abra o Sublime Text e vá para `Preferences > Package Settings > web-Live > Settings` para configurar o host e a porta desejados.

## Uso

- **Iniciar Servidor**: Use o painel de comandos (Ctrl+Shift+P) e procure por `web-live: start` para iniciar o servidor.
- **Parar Servidor**: Use o painel de comandos e procure por `web-live: stop` para parar o servidor.

## Configuração

Edite o arquivo `wlive.sublime-settings` para personalizar as configurações do servidor:

```json
{
    "host": "127.0.0.1",
    "port": "8080"
}
```

## Versão

- **Versão Atual**: 1.1

## Como Funciona

O plugin utiliza o `live-server` para servir arquivos e monitora as mudanças, reiniciando o servidor conforme necessário. No Linux, o PID do processo é gerenciado para garantir que o servidor possa ser interrompido corretamente.

## Suporte

Para problemas ou solicitações de funcionalidades, abra uma issue no repositório GitHub.

## Licença

Este projeto está licenciado sob a Licença MIT.

---

Sinta-se à vontade para ajustar conforme necessário!

