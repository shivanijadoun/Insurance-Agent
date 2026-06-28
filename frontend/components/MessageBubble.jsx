import React from "react";

export default function MessageBubble({ message }) {
  const isUser = message.role === "user";

  return (
    <div
      className={`flex w-full mb-4 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {/* Avatar */}
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-[#10a37f] flex items-center justify-center text-white mr-2">
          🤖
        </div>
      )}

      {/* Bubble */}
      <div
        className={`max-w-[70%] px-4 py-3 rounded-2xl text-sm leading-relaxed whitespace-pre-wrap ${
          isUser
            ? "bg-[#2563eb] text-white rounded-br-sm"
            : "bg-[#2f2f2f] text-white rounded-bl-sm"
        }`}
      >
        {message.text}
      </div>

      {/* User Avatar */}
      {isUser && (
        <div className="w-8 h-8 rounded-full bg-[#2563eb] flex items-center justify-center text-white ml-2">
          👤
        </div>
      )}
    </div>
  );
}