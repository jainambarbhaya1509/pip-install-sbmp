toast = '''
    Toast.makeText(RadioBtnAct.this , "Selected option : " + rdbtn.getText(), Toast.LENGTH_SHORT).show();

'''

listview = '''
Java code :
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class ListAct extends AppCompatActivity {
    ListView listView;
    String[] items = {"Item 1", "Item 2", "Item 3", "Item 4"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list);
        listView = findViewById(R.id.listView);
//        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, items);
//        listView.setAdapter(adapter);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1,items);
        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                if(position == 1){
                Intent i = new Intent(ListAct.this, loginFormAct.class);
                startActivity(i);}
                else if (position == 2){
                    Intent i = new Intent(ListAct.this, SharedPrefAct.class);
                    startActivity(i);

                }
            }
        });


    }

}

xml code

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".ListAct">

    <ListView
        android:id="@+id/listView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        />

</androidx.constraintlayout.widget.ConstraintLayout>


'''

checkbox = '''

java :
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.CheckBox;
import android.widget.Toast;

public class checkBox extends AppCompatActivity {
    CheckBox checkBox1, checkBox2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_check_box);
        checkBox1 = findViewById(R.id.checkBox1);
        checkBox2 = findViewById(R.id.checkBox2);
        checkBox1.setOnCheckedChangeListener((buttonView, isChecked) ->
                Toast.makeText(this, "option1", Toast.LENGTH_SHORT).show());

        checkBox2.setOnCheckedChangeListener((buttonView, isChecked) ->
                Toast.makeText(this, "option2", Toast.LENGTH_SHORT).show());

    }
}


xml :
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".checkBox">

    <CheckBox
        android:id="@+id/checkBox1"
        android:layout_width="91dp"
        android:layout_height="40dp"
        android:text="Option 1"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <CheckBox
        android:id="@+id/checkBox2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Option 2"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/checkBox1" />


</androidx.constraintlayout.widget.ConstraintLayout>



'''

dateTime = '''
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.TextView;
import android.widget.TimePicker;

import java.util.Calendar;

public class dateTimeAct extends AppCompatActivity {
    TextView tvDate1, tvTime2;
    int d1Year, d1Month, d1Day, t2Hour, t2Minute;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_date_time);
        tvDate1 = findViewById(R.id.tv_date1);
        tvTime2 = findViewById(R.id.tv_date2);

        // Set OnClickListener for the first date TextView
        tvDate1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Initialize DatePickerDialog
                Calendar calendar = Calendar.getInstance();
                d1Year = calendar.get(Calendar.YEAR);
                d1Month = calendar.get(Calendar.MONTH);
                d1Day = calendar.get(Calendar.DAY_OF_MONTH);

                DatePickerDialog datePickerDialog = new DatePickerDialog(
                        dateTimeAct.this,
                        new DatePickerDialog.OnDateSetListener() {
                            @Override
                            public void onDateSet(DatePicker view, int year, int month, int dayOfMonth) {
                                // Update year, month, and day
                                d1Year = year;
                                d1Month = month;
                                d1Day = dayOfMonth;

                                // Set selected date in TextView
                                tvDate1.setText(dayOfMonth + "/" + (month + 1) + "/" + year);
                            }
                        }, d1Year, d1Month, d1Day);
                datePickerDialog.show();
            }
        });

        // Set OnClickListener for the second date TextView
        tvTime2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Initialize TimePickerDialog
                Calendar calendar = Calendar.getInstance();
                t2Hour = calendar.get(Calendar.HOUR_OF_DAY);
                t2Minute = calendar.get(Calendar.MINUTE);

                TimePickerDialog timePickerDialog = new TimePickerDialog(
                        dateTimeAct.this,
                        new TimePickerDialog.OnTimeSetListener() {
                            @Override
                            public void onTimeSet(TimePicker view, int hourOfDay, int minute) {
                                // Update hour and minute
                                t2Hour = hourOfDay;
                                t2Minute = minute;

                                // Set selected time in 12-hour format
                                tvTime2.setText(String.format("%02d:%02d %s",
                                        (t2Hour % 12 == 0 ? 12 : t2Hour % 12), t2Minute, (t2Hour < 12 ? "AM" : "PM")));
                            }
                        }, t2Hour, t2Minute, false); // 'false' for 12-hour format
                timePickerDialog.show();
            }
        });
    }
}

xml:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/tv_date1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Select Date 1"
        android:textSize="32sp"
        android:textStyle="bold"
        android:gravity="center"
        android:drawablePadding="16dp"
        android:background="@android:drawable/editbox_background"
        android:padding="16dp"/>

    <TextView
        android:id="@+id/tv_date2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Select Date 2"
        android:textSize="32sp"
        android:textStyle="bold"
        android:gravity="center"
        android:drawablePadding="16dp"
        android:background="@android:drawable/editbox_background"
        android:padding="16dp"
        android:layout_marginTop="16dp"/>

</LinearLayout>


'''

oneActToOtherAndToast = ''' 

package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    Button btn1, btn2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn1.findViewById(R.id.button);
        btn2.findViewById(R.id.button2);

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this,"Toast Msg",Toast.LENGTH_LONG).show();
            }
        });
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(MainActivity.this, SharedPrefAct.class);
                startActivity(i);

            }
        });

    }
}

xml:

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView" />
    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Next"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/button" />

</androidx.constraintlayout.widget.ConstraintLayout>
'''

radiobtn='''
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class RadioBtnAct extends AppCompatActivity {
   RadioGroup rdgrp;
   RadioButton rdbtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_radio_btn);


        rdgrp = findViewById(R.id.rdgrp);
        rdgrp.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                rdbtn = findViewById(checkedId);
                Toast.makeText(RadioBtnAct.this , "Selected option : " + rdbtn.getText(), Toast.LENGTH_SHORT).show();
            }
        });


    }
}

xml:
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".RadioBtnAct">

    <RadioGroup
        android:id="@+id/rdgrp"

        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent">


        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="opt 1"/>
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="opt 2"/>
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="opt 3"/>

    </RadioGroup>
</androidx.constraintlayout.widget.ConstraintLayout>

'''

sharedPrefrence='''
package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SharedPrefAct extends AppCompatActivity {
    EditText editTextUsername;
    Button buttonSave;

    ListView listViewUsernames;

    ArrayAdapter<String> adapter;
    List<String> usernameList ;

    SharedPreferences sharedPreferences;
    SharedPreferences.Editor editor;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shared_pref);
        editTextUsername = findViewById(R.id.editTextUsername);
        buttonSave = findViewById(R.id.buttonSave);
        listViewUsernames = findViewById(R.id.listViewUsernames);

        // Initialize SharedPreferences
        sharedPreferences = getSharedPreferences("MyPref", Context.MODE_PRIVATE);
        editor = sharedPreferences.edit();

        // Initialize the list and adapter
        usernameList = new ArrayList<>();
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, usernameList);
        listViewUsernames.setAdapter(adapter);

        // Load previously saved usernames and update the ListView
        loadUsernames();

        // Set up the Save button's OnClickListener
        buttonSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String username = editTextUsername.getText().toString().trim();

                if (!username.isEmpty()) {
                    // Save username to SharedPreferences
                    saveUsername(username);
                    // Clear the input field
                    editTextUsername.setText("");
                    // Show confirmation message
                    Toast.makeText(SharedPrefAct.this, "Username saved!", Toast.LENGTH_SHORT).show();
                    // Update the ListView with the new username
                    loadUsernames();
                } else {
                    Toast.makeText(SharedPrefAct.this, "Please enter a username", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    // Function to save username to SharedPreferences
    private void saveUsername(String username) {
        // Retrieve existing usernames from SharedPreferences
        Set<String> usernameSet = sharedPreferences.getStringSet("usernames", new HashSet<>());

        // Add the new username
        usernameSet.add(username);

        // Save the updated set back to SharedPreferences
        editor.putStringSet("usernames", usernameSet);
        editor.apply();  // Apply changes
    }

    // Function to load usernames from SharedPreferences and update the ListView
    private void loadUsernames() {
        // Clear the current list
        usernameList.clear();

        // Retrieve the usernames from SharedPreferences
        Set<String> usernameSet = sharedPreferences.getStringSet("usernames", new HashSet<>());

        // Add all usernames to the list
        usernameList.addAll(usernameSet);

        // Notify the adapter to refresh the ListView
        adapter.notifyDataSetChanged();
    }
}


xml:

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".SharedPrefAct">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:padding="16dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent">

        <EditText
            android:id="@+id/editTextUsername"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter username" />

        <Button
            android:id="@+id/buttonSave"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Save" />
        <ListView
            android:id="@+id/listViewUsernames"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

</androidx.constraintlayout.widget.ConstraintLayout>


'''

loginForm = '''
java code :

package com.example.practical;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class loginFormAct extends AppCompatActivity {
    EditText username, password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_form);
        username = findViewById(R.id.username);
        password = findViewById(R.id.password);
    }

    public void login(View view) {
        String user = username.getText().toString();
        String pass = password.getText().toString();

        if (user.equals("admin") && pass.equals("admin")) {
            Toast.makeText(this, "Login successful", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Invalid credentials", Toast.LENGTH_SHORT).show();
        }
    }
}

xml:


<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".loginFormAct">


    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">
        <EditText
            android:id="@+id/username"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Username" />

        <EditText
            android:id="@+id/password"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Password"

            android:inputType="textPassword" />

        <Button
            android:id="@+id/loginButton"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Login" />

    </LinearLayout>

</androidx.constraintlayout.widget.ConstraintLayout>


'''

lifecycle = '''
act1 java:
package com.example.activitylifecycle2;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(this, "onCreate", Toast.LENGTH_SHORT).show();
        
        // Set up the TextView to navigate to SecondActivity
        TextView textView = findViewById(R.id.FirstActivity);
        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                startActivity(intent);
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast.makeText(this, "onStart", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        Toast.makeText(this, "onResume", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast.makeText(this, "onPause", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onStop() {
        super.onStop();
        Toast.makeText(this, "onStop", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast.makeText(this, "onRestart", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Toast.makeText(this, "onDestroy", Toast.LENGTH_SHORT).show();
    }
}


act1 xml:
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/FirstActivity"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="First Activity!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>


act2 java:
package com.example.activitylifecycle2;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        Toast toast = Toast.makeText(this, "SecondCreate", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();

        // Set up the TextView to navigate to ThirdActivity
        TextView textView = findViewById(R.id.SecondActivity);
        textView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(SecondActivity.this, ThirdActivity.class);
                startActivity(intent);
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast toast = Toast.makeText(this, "SecondStart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        Toast toast = Toast.makeText(this, "SecondResume", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast toast = Toast.makeText(this, "SecondPause", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onStop() {
        super.onStop();
        Toast toast = Toast.makeText(this, "SecondStop", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast toast = Toast.makeText(this, "SecondRestart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Toast toast = Toast.makeText(this, "SecondDestroy", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.CENTER, 0, 0);
        toast.show();
    }
}

act2 xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".SecondActivity">

    <TextView
        android:id="@+id/SecondActivity"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Second Activity!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>


act3 java:
package com.example.activitylifecycle2;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.widget.Toast;

public class ThirdActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third);
        Toast toast = Toast.makeText(this, "ThirdCreate", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast toast = Toast.makeText(this, "ThirdStart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        Toast toast = Toast.makeText(this, "ThirdResume", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onPause() {
        super.onPause();
        Toast toast = Toast.makeText(this, "ThirdPause", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onStop() {
        super.onStop();
        Toast toast = Toast.makeText(this, "ThirdStop", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast toast = Toast.makeText(this, "ThirdRestart", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Toast toast = Toast.makeText(this, "ThirdDestroy", Toast.LENGTH_SHORT);
        toast.setGravity(Gravity.TOP, 0, 0);
        toast.show();
    }
}


act3 xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".ThirdActivity">

    <TextView
        android:id="@+id/ThirdActivity"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Third Activity!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>



'''

fluterexp1 = '''
import 'package:flutter/material.dart';

class HelloWorld extends StatefulWidget {
  const HelloWorld({super.key});

  @override
  State<HelloWorld> createState() => _HelloWorldState();
}

class _HelloWorldState extends State<HelloWorld> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Hello App"),
      ),
      body: Center(
        child: Text("Hello World!!"),
      ),
    );
  }
}
'''

flutterexp2 = '''
import 'package:flutter/material.dart';

class RowAndCol extends StatefulWidget {
  const RowAndCol({super.key});

  @override
  State<RowAndCol> createState() => _RowAndColState();
}

class _RowAndColState extends State<RowAndCol> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Rows"),
      ),
      body: Center(
        child: Row(
          children: [
            Column(
              children: [
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.red,
                ),
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.blue,
                ),
              ],
            ),
            Column(
              children: [
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.blue,
                ),
                Container(
                  height: 100,
                  width: 100,
                  color: Colors.red,
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}

'''

mob_codes = {
    "toast.txt": toast,
    "listview.txt": listview,
    "checkbox.txt": checkbox,
    "dateTime.txt": dateTime,
    "oneActToOther.txt": oneActToOtherAndToast,
    'radiobtn.txt': radiobtn,
    'sharedPref.txt': sharedPrefrence,
    'loginForm.txt': loginForm,
    'lifecycle.txt': lifecycle,
    'flutter1.txt':fluterexp1,
    'flutter2.txt':flutterexp2

}



def mob_():
    for file,code in mob_codes.items():
        print(file)
    filename = input("Enter filename: ")
    with open(filename, 'w') as f:
        f.write(mob_codes[filename])
        


    