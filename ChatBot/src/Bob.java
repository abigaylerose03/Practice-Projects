import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import java.util.Random;
import java.util.Scanner;

public class Bob extends JFrame {
	
	String[] bobHRU = {"I am good! :D", "Eh, not so good. I'm really sick *coughs*", 
						"Pretty good, I'm tired of answering questions already.."
			
	};
	
	String[] bobFood = {"My favorite food is cottage cheese with kethchup. Yummy right?",
						"Not sure, but I love taking bites of potato chips!!!"
	};

	
	
	String[] bobFoodAnswer = {"Wow!!! That's neat.", "I've never tried that before.", 
							  "Sounds delicious!"
	};
	
	String[] bobSing = {"Ummm, I'm just a chatbot..I can't sing", "Who do you think I am?", 
						"Here goes nothing! mASK ON beep beep MASK OFF"
																											
	};
	
	String[] bobWU = {"Just listening to your personal problems :)", "The ground", 
					 "Evaluating my databases, reinstalling a VPN for my desktop PC, and "
					 + " converting utf-8 to utf-16...y'know the usual!"
	};
	
	String[] bobSiri = {"Yeah, we go wayyy back.", "Siri who? My rival chatbot??", 
						"Ahh Siri..my cousin's nephew's granparent's son's girlfriend. And also, "
						+ " my arch enemy!"
	};
	
	String[] bobDefault = {"Mhmmmm", "I am afriad I can't answer that", "I'm afraid I can't answer that", "zzz, what did you say?",
								"Yeah, life is that way sometimes.", "Really? Wow", "Don't be so mean"
	};
	
	
	// --Typing Area--
	private JTextField txtEnter = new JTextField();
	
	// --Chat Area--
	private JTextArea txtChat = new JTextArea();
	
	
	String bobGreeting = "Hi there! My name is Bob. Your neighbor-friendly chat bot!!!\n "
								+ "\t You can ask me questions like:\n "
								+ "\t How are you?\n "
								+ "\t What's your favorite food?\n "
								+ "\t Sing me a song\n"
								+ "\t What's up?\n"
								+ "\t And even, 'Do you know Siri?'\n";
	
	
	public Bob() {
		
		// Frame attributes:
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setSize(700, 1600);
		this.setVisible(true);
		this.setResizable(false);
		this.setLayout(null);
		this.setTitle("Bob the ChatBot");
		
		// txtEnter Attributes
		txtEnter.setLocation(2, 540);
		txtEnter.setSize(590, 30);
		txtEnter.setEditable(true);
		
		// txtChat Attributes:
		txtChat.setLocation(15, 5);
		txtChat.setSize(560, 350);
		txtChat.setEditable(false);
		
		
		// txtEnter Action Event
		txtEnter.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent a) {
				String uText = txtEnter.getText();// .substring(0, 1).toUpperCase().substring(1);
				txtChat.append("-->You: " + uText + "\n");
				
				switch(uText) {
				
					case "hello":
						botSays(bobGreeting);
						break;
						
					case "hi":
						botSays(bobGreeting);
						break;
					
					case "hey":
						botSays(bobGreeting);
						break;
					
					case "what's up?":
						botSays(rand_arr(bobWU));
						break;
					
					case "do you know Siri?":
						botSays(rand_arr(bobSiri));
						break;
					
					case "sing me a song":
						botSays(rand_arr(bobSing));
						break;
						
					case "how are you?":
						botSays(rand_arr(bobHRU));
						break;
					
					case "what's your favorite food?":
						botSays(rand_arr(bobFood));
						break;
					
					default:
						botSays(rand_arr(bobDefault));
						break;
				} txtEnter.setText("");
				
			}
			
		});
		
		
		// add the items to the JFrame class
		this.add(txtEnter);
		this.add(txtChat);
		
		
	}
	
							  
	
	
	
	
	public String rand_arr(String[] arr) {
		int rdn = new Random().nextInt(arr.length);
		return arr[rdn];
	}
	
	public void botSays(String s) {
		txtChat.append("-->Mc Minion: " + s + "\n");
	}
	
	public static void main(String[] args) {
		new Bob(); 
	}
	
}
