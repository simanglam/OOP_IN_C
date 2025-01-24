abstract class FileImage {
	private Pixale[][] data;
	Pixale pixaleAt(int x, int y) {/* */}
	public void setPixaleAt(int x, int y, Pixale p) {/* */}
	public void resize(int x, int y) {/* */}
	public abstract void save();
	public abstract void load();
}