package hm8;
/*
 * Malia Clifton
 * CSC 1302
 * Homework 05
 */
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
public class JInsurance extends JFrame implements ItemListener {
	private static final long serialVersionUID = 1L;
	FlowLayout flow = new FlowLayout();
    ButtonGroup insGrp = new ButtonGroup();
    JCheckBox hmo = new JCheckBox("HMO", false);
    JCheckBox ppo = new JCheckBox("PPO", false);
    JCheckBox dental = new JCheckBox("Dental", false);
    JCheckBox vision = new JCheckBox("Vision", false);
    JTextField insChoice = new JTextField(20);
    static int HMOPRICE = 200;
    static int PPOPRICE = 600;
    static int DENTALPRICE = 75;
    static int VISIONPRICE = 20;

    String output, insChosen;
    public JInsurance() {
        super("Ex8 - Check Boxes");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(flow);
        insGrp.add(hmo); insGrp.add(ppo);
        add(hmo);
        add(ppo);
        add(dental);
        add(vision);
        add(insChoice);
     
        hmo.addItemListener(this);
        ppo.addItemListener(this);
        dental.addItemListener(this);
        vision.addItemListener(this);
    }
    public static void main(String[] arguments) {
        JInsurance iFrame = new JInsurance();
        iFrame.setSize(400, 100);
        iFrame.setVisible(true);
    }
    @Override
    public void itemStateChanged(ItemEvent check) {
    	output="";
        if(hmo.isSelected())
            output=String.valueOf("HMO $"+HMOPRICE + " ");    
        if(ppo.isSelected())
            output=String.valueOf("PPO $"+PPOPRICE+ " ");
        if(dental.isSelected())
            output+=String.valueOf("Dental $"+DENTALPRICE+ " ");    
        if(vision.isSelected())
            output+=String.valueOf("Vision $"+VISIONPRICE+ " ");    
        insChoice.setText(output);
    	
    }
}