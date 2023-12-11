package Swing;

	import javax.swing.*;
	import java.awt.*;
	import java.awt.event.*;

	public class JHelloFrame2 extends JFrame {

		JLabel question=new JLabel("What is your name?");
		Font bigFont=new Font("Arial", Font.BOLD, 20);
		JTextField answer=new JTextField(28);
		JButton pressME=new JButton("Press ME");
		JButton endAPP=new JButton("Exit App.");
		JButton clearName=new JButton("Clear Name");
		JLabel greeting=new JLabel("");
		final int WIDTH=350;
		final int HEIGHT=220;
		
		public JHelloFrame2() {
			super("Hello Frame 2 Example");
			setSize(WIDTH, HEIGHT);
			setLayout(new FlowLayout());
			question.setFont(bigFont);
			greeting.setFont(bigFont);
			
			add(question);
			add(answer);
			add(pressME);
			add(greeting);
			add(endAPP);
			add(clearName);
			setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			pressME.addActionListener(new Greeting_Action());
			endAPP.addActionListener(new EndAPP_Action());
			clearName.addActionListener(new ClearName_Action());
		}

		private class Greeting_Action implements ActionListener {
		     public void actionPerformed(ActionEvent e) {
		    	 String name = answer.getText();
		    	 greeting.setText("Hello "+name);
		     }
		}
		
		private class ClearName_Action implements ActionListener {
		     public void actionPerformed(ActionEvent e) {
		    	 answer.setText("");
		     }
		}

		private class EndAPP_Action implements ActionListener{
		     public void actionPerformed(ActionEvent e) {
		    	 System.exit(0);
		     }
		}
		
	}

