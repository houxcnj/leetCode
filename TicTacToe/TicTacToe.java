package TicTacToe;

class TicTacToe {
	private int[] rows;
	private int[] cols;
	private int dia;
	private int antiDia;

    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        rows = new int[n];
        cols = new int[n];
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.TicTacToe
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
    	int addon = player == 1 ? 1 : -1;
        
        rows[row] += addon;
        cols[col] += addon;
        
        if (row == col) {
            dia += addon;
        }
        if (row + col == rows.length - 1) {
            antiDia += addon;
        }
        
        int len = rows.length;
        if (Math.abs(rows[row]) == len || Math.abs(cols[col]) == len ||
           Math.abs(dia) == len || Math.abs(antiDia) == len) {
            return player;
        }
        return 0;
    }
}
