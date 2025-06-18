import React, { useState, useEffect } from 'react';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    // Aquí se puede implementar la lógica para recibir mensajes del backend
    const fetchMessages = async () => {
      const response = await fetch('http://localhost:8000/api/chat/messages');
      const data = await response.json();
      setMessages(data.messages);
    };

    fetchMessages();
  }, []);

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (input.trim() === '') return;

    // Aquí se puede implementar la lógica para enviar un mensaje al backend
    const response = await fetch('http://localhost:8000/api/chat/send', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: input }),
    });

    if (response.ok) {
      setInput('');
      // Actualizar la lista de mensajes después de enviar
      const newMessage = { text: input, sender: 'You' };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className="chat-message">
            <strong>{msg.sender}: </strong>{msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSendMessage} className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Escribe un mensaje..."
        />
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
};

export default Chat;