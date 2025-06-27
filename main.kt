import java.util.concurrent.ConcurrentHashMap

class Memoize(private val m:ConcurrentHashMap<Int,Int>){
    init{
        m[0]=1
        m[-1]=1
    }
    fun f(i:Int):Int{
        if(m[i]!=null){
            return m[i]!!
        }else{
            m.putIfAbsent(i,f(i-1)+f(i-2))
            return m[i]!!
        }
    }

}

fun main(){
    val m= ConcurrentHashMap<Int,Int>()
    val memoize=Memoize(m)
    print(memoize.f(4))

}