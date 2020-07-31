public class HiddenWord {
	
	private String word;
	
	public HiddenWord(String hWord) {
		word = hWord;
	}
	
	/*
	 * @param guess: the user's guess of the hidden word
	 * @param hint: the user's hint
	 * @param word: the hidden word 
	 */
	
	public String getHint(String guess) {
		String hint = "";
		for(int i = 0; i < guess.length(); i++) {
			if(guess.substring(i, i + 1).equals(word.substring(i, i + 1))) {
				hint += guess.substring(i, i + 1);
				
			} else if(word.indexOf(guess.substring(i, i + 1)) != - 1) {
				hint += "+";
			} else {
				hint += "*";
			}
		}
		return hint;
	}

}
