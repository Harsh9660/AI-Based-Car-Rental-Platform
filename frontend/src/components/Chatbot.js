import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [input, setInput] = useState('');
  const [conversation, setConversation] = useState([]);

  const sendMessage = async () => {
    if(input.trim() === '') return;
    setConversation(prev => [...prev, { user: true, text: input }]);
    try {
      const res = await axios.post('/api/chatbot', { message: input });
      setConversation(prev => [...prev, { user: false, text: res.data.reply }]);
    } catch {
      setConversation(prev => [...prev, { user: false, text: "Sorry, I can't respond right now." }]);
    }
    setInput('');
  };

  return (
    <div className="mt-8 border p-4 rounded max-w-md">
      <h2 className="text-xl font-semibold mb-4">Chatbot Assistant</h2>
      <div className="h-48 overflow-auto border p-2 mb-2">
        {conversation.map((msg, idx) => (
          <div key={idx} className={msg.user ? 'text-right' : 'text-left'}>
            <p className={`inline-block p-2 rounded ${msg.user ? 'bg-blue-200' : 'bg-gray-200'}`}>{msg.text}</p>
          </div>
        ))}
      </div>
      <input
        type="text"
        className="border p-2 w-full"
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && sendMessage()}
        placeholder="Ask me anything..."
      />
    </div>
  );
};

export default Chatbot;
