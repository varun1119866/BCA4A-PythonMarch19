import java.awt.*;
import java.awt.event.*;

public class MiniCalculator extends Frame implements ActionListener {
  private TextField num1Field, num2Field, resultField;
  private Button addButton, subButton, mulButton, divButton, modButton, submitButton, resetButton;

  public MiniCalculator() {
    setTitle("Mini Calculator");
    setBackground(Color.BLUE);
    setLayout(new GridLayout(3, 1));

    // First line: Number 1, Number 2, Result
    Panel inputPanel = new Panel(new GridLayout(1, 6));
    Label num1Label = new Label("Number 1:");
    num1Field = new TextField(10);
    Label num2Label = new Label("Number 2:");
    num2Field = new TextField(10);
    Label resultLabel = new Label("Result:");
    resultField = new TextField(10);
    resultField.setEditable(false); // Result field should not be editable
    inputPanel.add(num1Label);
    inputPanel.add(num1Field);
    inputPanel.add(num2Label);
    inputPanel.add(num2Field);
    inputPanel.add(resultLabel);
    inputPanel.add(resultField);
    add(inputPanel);

    // Second line: Buttons (MUL, ADD, SUB, DIV, MOD)
    Panel buttonPanel = new Panel(new GridLayout(1, 5));
    mulButton = new Button("MUL");
    addListenerToButton(mulButton);
    addButton = new Button("ADD");
    addListenerToButton(addButton);
    subButton = new Button("SUB");
    addListenerToButton(subButton);
    divButton = new Button("DIV");
    addListenerToButton(divButton);
    modButton = new Button("MOD");
    addListenerToButton(modButton);
    buttonPanel.add(mulButton);
    buttonPanel.add(addButton);
    buttonPanel.add(subButton);
    buttonPanel.add(divButton);
    buttonPanel.add(modButton);
    add(buttonPanel);

    // Third line: Submit and Reset buttons
    Panel controlPanel = new Panel(new GridLayout(1, 2));
    submitButton = new Button("SUBMIT");
    submitButton.addActionListener(this);
    resetButton = new Button("RESET");
    resetButton.addActionListener(this);
    controlPanel.add(submitButton);
    controlPanel.add(resetButton);
    add(controlPanel);

    // Window properties
    setSize(400, 150);
    setLocationRelativeTo(null); // Center the window
    setVisible(true);
  }

  private void addListenerToButton(Button button) {
    button.addActionListener(this);
  }

  @Override
  public void actionPerformed(ActionEvent e) {
    int num1 = Integer.parseInt(num1Field.getText());
    int num2 = Integer.parseInt(num2Field.getText());
    int result = 0;
    String operator = e.getActionCommand();

    switch (operator) {
      case "MUL":
        result = num1 * num2;
        break;
      case "ADD":
        result = num1 + num2;
        break;
      case "SUB":
        result = num1 - num2;
        break;
      case "DIV":
        if (num2 != 0) {
          result = num1 / num2;
        } else {
          resultField.setText("Error: Division by zero!");
          return;
        }
        break;
      case "MOD":
        result = num1 % num2;
        break;
      case "SUBMIT":
        // Do nothing when Submit button is clicked
        return;
      case "RESET":
        num1Field.setText("");
        num2Field.setText("");
        resultField.setText("");
        return;
    }

    resultField.setText(String.valueOf(result));
  }

  public static void main(String[] args) {
    new MiniCalculator();
  }
}
