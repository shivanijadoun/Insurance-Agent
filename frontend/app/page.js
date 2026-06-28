import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";

export default function Home() {
  return (
    <div className="flex h-screen w-full">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Chat Area */}
      <div className="flex-1">
        <ChatWindow />
      </div>

    </div>
  );
}